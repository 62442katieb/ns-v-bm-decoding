function ImgExps = BMA_ImageSearch()
    addpath /home/applications/spm12
    load('BrainMapMetaData_NormalActs.mat')
    filename = spm_select;
    tempimg = spm_read_vols(spm_vol((filename)));
    for a = 1:max(tempimg(:))
        locs = find(tempimg==a);
        [newloc(:,1), newloc(:,2), newloc(:,3)] = ind2sub(size(tempimg), locs);
        for b = 1:numel(Experiments)
            if size(tempimg) == [80 96 70]
                coords = Experiments(b).XYZ_Tal;
            else
                coords = Experiments(b).XYZ_MNI;
            end
            tempdist = min(pdist2(newloc, coords), [], 2);
            if length(find(tempdist<1.5))>0
                check2(b) = 1;
            else
                check2(b) = 0;
            end
            clear tempdist coords
        end
        ImgExps{a} = Experiments(find(check2));
        clear locs newloc
    end